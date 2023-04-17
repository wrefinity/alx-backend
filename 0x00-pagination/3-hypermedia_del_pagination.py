#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination
"""
import csv
from typing import Dict, List


class Server:
    """Server class of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                dt = csv.reader(f)
                dataset = [rw for rw in dt]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """sort the position
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ get page information based on a page number.
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())
        p_data = []
        data_count = 0
        next_index = None
        start = index if index else 0
        for i, item in data.items():
            if i >= start and data_count < page_size:
                p_data.append(item)
                data_count += 1
                continue
            if data_count == page_size:
                next_index = i
                break
        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(p_data),
            'data': p_data,
        }
        return page_info

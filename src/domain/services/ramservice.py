"""
This module defines a controller class for fetching CPU values from a monitoring task.
"""
from typing import List
from domain.models import Ram
from monitor import MonitorTask


# Controller class to fetch cpu values from monitoring task
class RamService:
    """
    Controller class to fetch CPU values from a monitoring task.
    """

    def __init__(self):
        ...

    async def get_ram(self, monitor_task: MonitorTask) -> Ram:
        """
        Get CPU values from the provided monitoring task and return them as a list of Cpu objects.

        Args:
            monitor_task (MonitorTask): The monitoring task to fetch CPU data from.

        Returns:
            List[Cpu]: A list of Cpu objects containing CPU values.
        """
        vm = monitor_task.virtual_memory
        ram = Ram(
            id=0,
            total=vm.total,
            available=vm.available,
            used=vm.used,
            percent=vm.percent
        )
        return ram

    def __str__(self):
        return self.__class__.__name__

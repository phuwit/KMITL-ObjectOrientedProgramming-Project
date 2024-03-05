from typing import List, Union
import uuid

from backend.definitions.course import Course
from backend.definitions.progress import Progress
from backend.definitions.order import Order

class User:
    # Constants
    FETCH_SEARCH_MAX = 10

    def __init__(self, name: str) -> None:
        self.__id = uuid.uuid4()
        self.__name = name
        self.__my_progresses: List[Progress] = []
        self.__latest_progress: Union[Progress, None] = None
        self.__address = None
        self.__payment_method = None
        self.__orders: List[Order] = []

    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name

    def get_latest_video_from_user(self):
        if self.__latest_progress is None:
            return None
        latest_progress_video = self.__latest_progress.get_latest_video()
        return latest_progress_video

    def search_progress_by_name(self, name: str):
        for progress in self.__my_progresses:
            if progress.get_name() == name:
                return progress
        return None

    def set_latest_progress(self, progress: Progress):
        self.__latest_progress = progress

    def add_progress(self, progress: Progress):
        self.__my_progresses.append(progress)   

    def view_my_learning(self):
        # Fetch at most FETCH_SEARCH_MAX progress items
        return self.__my_progresses[:User.FETCH_SEARCH_MAX]
    
    def view_video_by_url(self, url : str):
        for progress in self.__my_progresses:
            video = progress.search_video_by_url(url)
            if video != None:
                return video
    def view_video_by_name(self, name: str):
        for progress in self.__my_progresses:
            video = progress.search_video_by_name(name)
            if video != None:
                return video
        return None#"Video not found please check your input"
    
    def set_address(self, address):
        self.__address = address
        
    def set_pament_method(self, payment_method):
        self.__payment_method = payment_method
        
    def get_address(self):
        return self.__address
    
    def get_payment_method(self):
        return self.__payment_method
    
    def get_orders(self):
        return self.__orders

class Teacher(User):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__my_teachings: List[Course] = []
        
    def get_my_teachings(self):
        return self.__my_teachings
    
    def add_my_teaching(self, course: Course):
        if(isinstance(course, Course)):
            self.__my_teachings.append(course)
            return True
        return False

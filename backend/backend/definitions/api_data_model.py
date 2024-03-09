from pydantic import BaseModel
from uuid import UUID

class CourseCardData(BaseModel):
    id: str
    name: str
    description: str
    price: float
    rating: float
    banner_image: str

class CourseCardDataWithLabel(BaseModel):
    id: str
    label: str
    cards: list[CourseCardData]


class CourseInfo(BaseModel):
    id: str
    name: str
    description: str
    category_id: str
    category_name: str
    price: float
    rating: float
    banner_image: str
    materials_images: list[str]
    materials_quizes: list[str]
    materials_videos: list[str]

class CourseLearnMaterial(BaseModel):
    id: str
    name: str
    description: str

class CourseLearnMaterialQuizQuestions(BaseModel):
    id: str
    question: str

class AnswerQuestion(BaseModel):
    ids: list[UUID]

class CourseLearnMaterialQuiz(CourseLearnMaterial):
    id: str
    name: str
    description: str
    questions: list[CourseLearnMaterialQuizQuestions]

class CourseLearnMaterialImage(CourseLearnMaterial):
    id: str
    name: str
    description: str
    url: str

class CourseLearnMaterialVideo(CourseLearnMaterial):
    id: str
    name: str
    description: str
    url: str

class CourseLearn(CourseInfo):
    learn_materials_quizes: list[CourseLearnMaterialQuiz]
    learn_materials_images: list[CourseLearnMaterialImage]
    learn_materials_videos: list[CourseLearnMaterialVideo]

class ProgressVideoData(BaseModel):
    id: UUID
    is_complete: bool

class CourseMaterialData(BaseModel):
    name: str
    description: str

class AddImageToCoursePostData(CourseMaterialData):
    url: str

class PostCourseData(BaseModel):
    name: str
    description: str
    price: int
    category_id: str

class QuizQuestionData(BaseModel):
    question: str
    correct: bool


class AddQuizToCoursePostData(CourseMaterialData):
    questions: list[QuizQuestionData]


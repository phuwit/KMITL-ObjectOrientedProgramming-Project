"use client";

import { useEffect, useState } from "react";
import { CourseCard } from "~/src/components/course/card";
import { getCoursesByTeachers } from "~/src/lib/data/teacher";
import { type CourseCardDataWithLabel } from "~/src/lib/definitions/course";

export default function CoursesByTeacher({
  params,
}: {
  params: { teacherID: string };
}) {
  const [cardsDataWithLabel, setCardsData] = useState<
    CourseCardDataWithLabel | null | undefined
  >(undefined);

  useEffect(() => {
    async function fetchData() {
      const apiData = await getCoursesByTeachers(params.teacherID);
      console.log(apiData);
      setCardsData(apiData);
    }
    void fetchData();
  }, []);

  return (
    <div className="flex w-full justify-center">
      <div className="w-full max-w-screen-lg space-y-4">
        <h1 className="text-3xl font-bold">{`Teacher ${cardsDataWithLabel?.label[0]?.toUpperCase()}${cardsDataWithLabel?.label.slice(1).toLowerCase()}`}</h1>
        <div className="grid grid-cols-4 gap-4">
          {cardsDataWithLabel?.cards.map((course) => {
            return <CourseCard key={course.id} course={course} />;
          })}
        </div>
      </div>
    </div>
  );
}
"use client";

import { useEffect, useState } from "react";
import * as XLSX from "xlsx";
import Link from "next/link";

export default function ExcelReader({ searchTerm }: { searchTerm: string }) {
  const [excelData, setExcelData] = useState<any[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetch("/Social_Media_Trends.xlsx");
      const ab = await res.arrayBuffer();
      const wb = XLSX.read(ab, { type: "buffer" });
      const ws = wb.Sheets[wb.SheetNames[0]];
      const data = XLSX.utils.sheet_to_json(ws);
      setExcelData(data);
    };

    fetchData();
  }, []);

  const filteredData = excelData.filter((entry) =>
    entry.Platform?.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="mt-3 mx-auto p-4 md:w-[70%] w-[100%]">
      {filteredData.map((entry, index) => (
        <div key={index} className="mb-2 p-2 rounded text-white bg-gray-800">
          <div className="flex justify-between items-start">
            <div>
              <Link href={`/details/${index}`}>
                <p className="hover:underline cursor-pointer font-semibold">
                  {entry.Platform}
                </p>
              </Link>
              <Link href={`/details/${index}`}>
                <p className="hover:underline cursor-pointer">
                  Post: {entry.Text}
                </p>
              </Link>
            </div>

            <Link href={`/edit/${index}`}>
              <button className="text-white text-xl px-2">...</button>
            </Link>
          </div>
          <div className="w-full h-[2px] bg-white my-4"></div>
        </div>
      ))}
    </div>
  );
}

"use client";

import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import * as XLSX from "xlsx";

export default function EditPage() {
  const { id } = useParams();
  const [data, setData] = useState<any | null>(null);
  const [hasChanged, setHasChanged] = useState(false);

  useEffect(() => {
    const loadData = async () => {
      const res = await fetch("/Social_Media_Trends.xlsx");
      const ab = await res.arrayBuffer();
      const wb = XLSX.read(ab, { type: "buffer" });
      const ws = wb.Sheets[wb.SheetNames[0]];
      const json = XLSX.utils.sheet_to_json(ws);
      setData(json[Number(id)]);
    };

    loadData();
  }, [id]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!data) return;
    setHasChanged(true); // mark as changed
    setData({ ...data, [e.target.name]: e.target.value });
  };

  const handleSave = async () => {
    try {
      const res = await fetch("/api/updateEntry", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, updatedEntry: data }),
      });

      if (!res.ok) throw new Error("Failed to update");

      alert("Data saved successfully!");
      setHasChanged(false);
    } catch (err) {
      console.error(err);
      alert("Failed to save data.");
    }
  };

  if (!data) return <div className="p-4 text-white">Loading...</div>;

  return (
    <div className="p-4 text-white bg-black">
      <h1 className="text-2xl font-bold mb-4">Edit Entry</h1>
      <div className="space-y-3">
        {Object.entries(data).map(([key, value]) => (
          <div key={key}>
            <label className="block mb-1 font-semibold">{key}</label>
            <input
              type="text"
              name={key}
              value={value as string}
              onChange={handleChange}
              className="w-full p-2 rounded bg-gray-800 border border-gray-600"
            />
          </div>
        ))}
      </div>

      {hasChanged && (
          
        <button
          className="mt-6 bg-green-600 p-2 mx-8 px-8 rounded hover:bg-green-700"
          onClick={handleSave}
          >
          Save
        </button>
      )}
    </div>
  );
}

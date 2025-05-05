import fs from 'fs';
import path from 'path';
import * as XLSX from 'xlsx'; // Correct way to import from the xlsx module

export async function POST(request: Request) {
  const data = await request.json();

  // Your existing logic here
  const filePath = path.resolve('public', 'Social_Media_Trends.xlsx');
  const workbook = XLSX.utils.book_new();
  // More XLSX operations
  
  try {
    XLSX.writeFile(workbook, filePath);
    console.log("File written successfully.");
  } catch (error) {
    console.error("❌ API ERROR:", error);
  }
  
  return new Response('Success');
}

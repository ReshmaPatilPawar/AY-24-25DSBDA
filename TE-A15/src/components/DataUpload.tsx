import React, { useCallback } from 'react';
import { ArrowLeft } from 'lucide-react';

interface DataUploadProps {
  onDataUploaded: (data: any[]) => void;
  onBack: () => void;
}

const DataUpload: React.FC<DataUploadProps> = ({ onDataUploaded, onBack }) => {
  const handleFileUpload = useCallback((event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
      const text = e.target?.result as string;
      const lines = text.split('\n');
      const headers = lines[0].split(',');
      
      const data = lines.slice(1).map(line => {
        const values = line.split(',');
        return headers.reduce((obj: any, header, index) => {
          obj[header.trim()] = parseFloat(values[index]);
          return obj;
        }, {});
      }).filter(row => Object.values(row).every(val => !isNaN(val)));

      onDataUploaded(data);
    };
    reader.readAsText(file);
  }, [onDataUploaded]);

  return (
    <div>
      <button 
        onClick={onBack}
        className="flex items-center text-gray-600 hover:text-gray-900 mb-6"
      >
        <ArrowLeft className="w-4 h-4 mr-2" />
        Back
      </button>

      <div className="max-w-xl mx-auto">
        <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center">
          <label className="block w-full cursor-pointer">
            <input
              type="file"
              accept=".csv"
              onChange={handleFileUpload}
              className="hidden"
            />
            <span className="inline-block px-4 py-2 bg-gray-900 text-white rounded-md hover:bg-gray-800">
              Choose CSV File
            </span>
            <p className="mt-2 text-gray-600">or drag and drop your file here</p>
          </label>
        </div>
      </div>
    </div>
  );
};

export default DataUpload;
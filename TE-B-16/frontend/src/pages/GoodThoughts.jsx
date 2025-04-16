import React, { useState, useEffect } from 'react';

const GoodThoughts = () => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');

  // Fetch messages from the backend
  useEffect(() => {
    fetch('/api/messages')
      .then((res) => res.json())
      .then((data) => setMessages(data));
  }, []);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (newMessage.trim()) {
      await fetch('/api/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: newMessage }),
      });
      setNewMessage('');
      // Refresh messages
      fetch('/api/messages')
        .then((res) => res.json())
        .then((data) => setMessages(data));
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Leave a Good Thought</h2>
      <form onSubmit={handleSubmit} className="mb-4">
        <textarea
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
          className="border p-2 w-full mb-2"
          rows="3"
          placeholder="Write something positive..."
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Post
        </button>
      </form>
      <h3 className="text-xl font-semibold">Messages from Others:</h3>
      <ul className="list-disc pl-5 mt-2">
        {messages.map((msg, index) => (
          <li key={index} className="mb-2">{msg.message}</li>
        ))}
      </ul>
    </div>
  );
};

export default GoodThoughts;

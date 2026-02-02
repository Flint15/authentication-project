import { useState } from "react";

export default function App() {
  const [response, setResponse] = useState<string>("");

  const sendRequest = async (): Promise<void> => {
    try {
      const response = await fetch("http://127.0.0.1:5000/love/Blue");
      const data = await response.text();
      setResponse(data);
    } catch (error) {
      console.error(`Error fetching data:\n ${error}`);
    }
  };

  return (
    <div className="main">
      <div className="response">
        {response ? response : "wait for response cutie"}
      </div>
      <button className="request-button" onClick={sendRequest}>
        Send request
      </button>
    </div>
  );
}

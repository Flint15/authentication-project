import { useState } from "react";

export default function App() {
  const [gmail, setGmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const sendRequest = async (): Promise<void> => {
    try {
      const response = await fetch("http://127.0.0.1:5000/api/data", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          gmail: gmail,
          password: password,
        }),
      });
      const result = await response.json();
      console.log(result);
    } catch (error) {
      console.error(`Error fetching data:\n ${error}`);
    }
  };

  return (
    <div className="main">
      <form>
        <label htmlFor="gmail">Gmail:</label>
        <input
          type="text"
          id="gmail"
          onChange={(e) => {
            setGmail(e.target.value);
          }}
        />
        <br />
        <label htmlFor="password">Password</label>
        <input
          type="text"
          id="password"
          onChange={(e) => {
            setPassword(e.target.value);
          }}
        />
      </form>
      <button className="request-button" onClick={sendRequest}>
        Send request
      </button>
    </div>
  );
}

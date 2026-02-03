import { useState } from "react";
import Form from "./components/Form";

export default function App() {
  const [gmail, setGmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const register = async (): Promise<void> => {
    try {
      const response = await fetch("http://127.0.0.1:5000/register", {
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
      <Form setGmail={setGmail} setPassword={setPassword} />
      <button className="register-button" onClick={register}>
        register
      </button>
    </div>
  );
}

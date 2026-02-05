import { useState } from "react";
import Form from "./components/Form";

export default function App() {
  const [gmail, setGmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [name, setName] = useState<string>("");
  const [signIn, setSignIn] = useState<boolean>(true);

  const register = async (): Promise<void> => {
    if (!gmail || password) return;
    try {
      const response = await fetch(
        `http://127.0.0.1:5000/${signIn ? "login" : "register"}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ ...(!signIn && { name }), gmail, password }),
        },
      );
      const result = await response.json();
      console.log(result);
    } catch (error) {
      console.error(`Error fetching data:\n ${error}`);
    }
  };

  return (
    <div className="main">
      <div className="login-buttons">
        <button
          className="sign-in"
          onClick={() => {
            setSignIn(true);
          }}
        >
          sign-in
        </button>
        <button
          className="sign-up"
          onClick={() => {
            setSignIn(false);
          }}
        >
          sign-up
        </button>
      </div>
      <Form
        signIn={signIn}
        setName={setName}
        setGmail={setGmail}
        setPassword={setPassword}
      />
      <button className="register-button" onClick={register}>
        {signIn ? "Sign In" : "Sign Up"}
      </button>
    </div>
  );
}

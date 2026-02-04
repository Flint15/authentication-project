import type { Dispatch, SetStateAction } from "react";

export default function Form({
  signIn,
  setName,
  setGmail,
  setPassword,
}: {
  signIn: boolean;
  setName: Dispatch<SetStateAction<string>>;
  setGmail: Dispatch<SetStateAction<string>>;
  setPassword: Dispatch<SetStateAction<string>>;
}) {
  return (
    <form>
      {!signIn && (
        <>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="gmail"
            onChange={(e) => {
              setName(e.target.value);
            }}
          />
          <br />
        </>
      )}
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
        type="password"
        id="password"
        onChange={(e) => {
          setPassword(e.target.value);
        }}
      />
    </form>
  );
}

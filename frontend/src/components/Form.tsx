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
            id="name"
            onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
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
        onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
          setGmail(e.target.value);
        }}
      />
      <br />
      <label htmlFor="password">Password</label>
      <input
        type="password"
        id="password"
        onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
          setPassword(e.target.value);
        }}
      />
    </form>
  );
}

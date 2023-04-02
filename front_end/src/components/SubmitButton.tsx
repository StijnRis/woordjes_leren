import React from "react";

interface Props {
  children: string;
}

const SubmitButton = ({ children }: Props) => {
  return <div className="button-submit">{children}</div>;
};

export default SubmitButton;

import React from "react";

interface Props {
  onClick: () => void;
}

const HintButton = ({ onClick }: Props) => {
  return (
    <div className="button-hint" onClick={onClick}>
      ?
    </div>
  );
};

export default HintButton;

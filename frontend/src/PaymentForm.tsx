import { useState } from "react";

interface Props {
  onSubmit: (value: number) => void;
}

export default function PaymentForm({ onSubmit }: Props) {
  const [raw, setRaw] = useState("");


  const handle = () => {
    const parsed = Number.parseFloat(raw) || 0;
    onSubmit(parsed);
  };

  return (
    <FormField>
      <input value={raw} onChange={(e) => setRaw(e.target.value)} />
      <button onClick={handle}>Pay</button>
    </FormField>
  );
}

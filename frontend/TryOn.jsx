import React, { useState } from 'react';

function TryOn() {
  const [email, setEmail] = useState('');

  const handleTryOn = async () => {
    await fetch('/api/fashion/try-on', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, item_id: '123' })
    });
    alert('Try-On Successful!');
  };

  return (
    <div>
      <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
      <button onClick={handleTryOn}>Try On</button>
    </div>
  );
}

export default TryOn;

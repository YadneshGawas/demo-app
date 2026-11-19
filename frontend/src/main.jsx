import React from "react";
import { createRoot } from "react-dom";
import axios from "axios";
import _ from "lodash";

function App() {
  const [message, setMessage] = React.useState("Loading API status...");
  React.useEffect(() => {
    axios.get("/api/status")
      .then((response) => setMessage(_.get(response, "data.message", "No message")))
      .catch(() => setMessage("Backend is not connected."));
  }, []);
  return <main>
    <h1>CodeGuard Vulnerable Demo</h1>
    <p>{message}</p>
    <p>This frontend intentionally pins outdated packages for scanner testing.</p>
  </main>;
}

createRoot(document.getElementById("root")).render(<App />);

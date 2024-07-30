import React from "react";
import { BrowserRouter as Router, Route, Routes} from "react-router-dom";
import EventsByType from "./EventsByType";
import EventDetail from "./EventDetail";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="events/:eventType" element={<EventsByType />} />
        <Route path="event/:slug" element={<EventDetail />} />
      </Routes>
    </Router>
  );
}

export default App;

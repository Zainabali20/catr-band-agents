import "./App.css";

function App() {
  const agents = [
    {
      step: "01",
      name: "Assessment Agent",
      role: "Extracts student profile",
      detail: "Reads raw student input and converts it into structured career guidance context.",
    },
    {
      step: "02",
      name: "Career Mapper Agent",
      role: "Maps career tracks",
      detail: "Recommends primary and alternative career paths based on interests and strengths.",
    },
    {
      step: "03",
      name: "Roadmap Planner Agent",
      role: "Builds academic roadmap",
      detail: "Creates Pakistan-specific subject, degree, exam, skill, and career planning guidance.",
    },
    {
      step: "04",
      name: "Review & Decision Agent",
      role: "Approves final roadmap",
      detail: "Reviews clarity, realism, risk level, and sends the final approved roadmap.",
    },
  ];

  return (
    <main className="page">
      <section className="hero">
        <div className="heroText">
          <p className="badge">Band-powered multi-agent workflow</p>
          <h1>CATR — Career Advisory Team for Pakistani Students</h1>
          <p className="subtitle">
            A multi-agent career guidance system where specialized agents assess,
            map, plan, review, and approve a student roadmap through Band.
          </p>

          <div className="heroActions">
            <a href="#workflow" className="primaryBtn">View Workflow</a>
            <a href="#roadmap" className="secondaryBtn">Sample Roadmap</a>
          </div>
        </div>

        <div className="studentCard">
          <p className="cardLabel">Sample Student</p>
          <h2>Hasan, 14</h2>
          <ul>
            <li><strong>Country:</strong> Pakistan</li>
            <li><strong>Interests:</strong> Computers, maths, business</li>
            <li><strong>Strong subjects:</strong> Mathematics, computer science</li>
            <li><strong>Weak subject:</strong> Chemistry</li>
            <li><strong>Dream job:</strong> Software engineer and entrepreneur</li>
          </ul>
        </div>
      </section>

      <section className="section" id="workflow">
        <div className="sectionHeader">
          <p className="eyebrow">Agent Collaboration</p>
          <h2>Not a single chatbot — a decision workflow</h2>
          <p>
            CATR uses Band as the collaboration layer. Each agent performs a
            separate role and passes structured context to the next agent.
          </p>
        </div>

        <div className="workflowGrid">
          {agents.map((agent) => (
            <div className="agentCard" key={agent.name}>
              <span className="step">{agent.step}</span>
              <h3>{agent.name}</h3>
              <p className="role">{agent.role}</p>
              <p>{agent.detail}</p>
            </div>
          ))}
        </div>

        <div className="handoffBox">
          <span>Band Handoff Flow</span>
          <code>
            Assessment → Career Mapper → Roadmap Planner → Review & Decision
          </code>
        </div>
      </section>

      <section className="section roadmapSection" id="roadmap">
        <div>
          <p className="eyebrow">Final Reviewed Output</p>
          <h2>Approved career roadmap</h2>
          <p className="muted">
            The final agent acts as a quality gate before the recommendation is
            delivered to the student or parent.
          </p>

          <div className="scoreCard">
            <h3>Quality Review Scorecard</h3>
            <ul>
              <li>Student-career fit: <strong>9/10</strong></li>
              <li>Pakistan relevance: <strong>9/10</strong></li>
              <li>Academic pathway clarity: <strong>9/10</strong></li>
              <li>Parent/student readability: <strong>9/10</strong></li>
              <li>Risk level: <strong>Low</strong></li>
              <li>Final decision: <strong>APPROVED</strong></li>
            </ul>
          </div>
        </div>

        <div className="roadmapCard">
          <h3>Recommended Path</h3>
          <p>
            Primary path: Software Engineering / Computer Science with early
            exposure to entrepreneurship.
          </p>

          <h3>Academic Roadmap</h3>
          <ul>
            <li>Matric: Maths, computer science, physics, English</li>
            <li>Intermediate: ICS or FSc Pre-Engineering</li>
            <li>Degree: BS Software Engineering, BS CS, BS AI/Data Science</li>
            <li>Entry prep: University admission tests and maths practice</li>
          </ul>

          <h3>Next 7 Days Action Plan</h3>
          <ul>
            <li>Day 1: Research Pakistani CS and software engineering degrees</li>
            <li>Day 2: Start Python basics</li>
            <li>Day 3: Practice maths problem solving</li>
            <li>Day 4: Check university admission requirements</li>
            <li>Day 5: Build a small calculator or quiz app</li>
            <li>Day 6: Discuss roadmap with parents or teacher</li>
            <li>Day 7: Create a monthly learning schedule</li>
          </ul>
        </div>
      </section>

      <section className="section finalSection">
        <h2>Why this fits the hackathon</h2>
        <div className="fitGrid">
          <div>
            <h3>Minimum 3 agents</h3>
            <p>CATR uses 4 specialized agents.</p>
          </div>
          <div>
            <h3>Meaningful Band usage</h3>
            <p>Agents hand off structured context through Band.</p>
          </div>
          <div>
            <h3>Review & decision-making</h3>
            <p>The final agent validates the roadmap before delivery.</p>
          </div>
        </div>
      </section>
    </main>
  );
}

export default App;
const uploadForm = document.querySelector("#upload-form");
const queryForm = document.querySelector("#query-form");
const uploadStatus = document.querySelector("#upload-status");
const queryStatus = document.querySelector("#query-status");
const previewTable = document.querySelector("#preview-table");
const datasetMeta = document.querySelector("#dataset-meta");
const answerBox = document.querySelector("#answer");
const engineNote = document.querySelector("#engine-note");
const chartNode = document.querySelector("#chart");

function setStatus(node, message, error=false) {
  node.textContent = message;
  node.classList.toggle("error", error);
}
function renderTable(rows) {
  previewTable.replaceChildren();
  if (!rows || !rows.length) return;
  const columns = Object.keys(rows[0]);
  const thead = document.createElement("thead");
  const headRow = document.createElement("tr");
  columns.forEach(c => { const th=document.createElement("th"); th.textContent=c; headRow.appendChild(th); });
  thead.appendChild(headRow);
  const tbody = document.createElement("tbody");
  rows.forEach(row => {
    const tr=document.createElement("tr");
    columns.forEach(c => { const td=document.createElement("td"); td.textContent=row[c] == null ? "" : String(row[c]); tr.appendChild(td); });
    tbody.appendChild(tr);
  });
  previewTable.append(thead, tbody);
}
uploadForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const file = document.querySelector("#csv-file").files[0];
  if (!file) return;
  setStatus(uploadStatus, "Uploading and validating CSV…");
  const formData = new FormData();
  formData.append("file", file);
  try {
    const response = await fetch("/api/upload", { method:"POST", body:formData });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Upload failed.");
    setStatus(uploadStatus, data.message);
    datasetMeta.textContent = `${data.rows.toLocaleString()} rows · ${data.columns.length} columns`;
    renderTable(data.preview);
    answerBox.textContent = "";
    engineNote.textContent = "";
    chartNode.replaceChildren();
  } catch (error) { setStatus(uploadStatus, error.message, true); }
});
queryForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const question = document.querySelector("#question").value.trim();
  if (!question) return;
  setStatus(queryStatus, "Analyzing…");
  answerBox.textContent = "";
  engineNote.textContent = "";
  chartNode.replaceChildren();
  try {
    const response = await fetch("/api/query", {
      method:"POST", headers:{"Content-Type":"application/json"},
      body:JSON.stringify({question})
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Query failed.");
    setStatus(queryStatus, "Analysis complete.");
    answerBox.textContent = data.answer || "No answer returned.";
    engineNote.textContent = `${data.engine || "Analysis"}${data.note ? " · " + data.note : ""}`;
    if (data.chart_json) {
      // The API returns Plotly figure JSON. Render it with Plotly when available.
      const figure = JSON.parse(data.chart_json);
      if (window.Plotly) {
        Plotly.newPlot(chartNode, figure.data || [], figure.layout || {}, {responsive:true, displaylogo:false});
      } else {
        // Chart.js fallback for simple bar/line data.
        const trace = (figure.data || [])[0];
        if (trace) {
          const canvas = document.createElement("canvas");
          chartNode.appendChild(canvas);
          new Chart(canvas, {type:trace.type === "bar" ? "bar" : "line",
            data:{labels:trace.x || [], datasets:[{label:trace.name || trace.y, data:trace.y || []}]},
            options:{responsive:true}});
        }
      }
    }
  } catch (error) { setStatus(queryStatus, error.message, true); }
});
document.querySelectorAll(".sample").forEach(button => {
  button.addEventListener("click", () => {
    document.querySelector("#question").value = button.textContent;
  });
});

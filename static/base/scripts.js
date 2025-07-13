document.addEventListener("DOMContentLoaded", function() {
    function toggleSubRows(mainRowPrefix) {
        const mainRows = document.querySelectorAll(`[id^='${mainRowPrefix}-']`);

        mainRows.forEach(function(mainRow) {
            mainRow.addEventListener("click", function() {
                // Extract the index from the main row ID (e.g., openmain-1 -> 1)
                const index = mainRow.id.split('-')[1];
                // Select all sub-rows with IDs starting with sub-<index>-
                const subs = document.querySelectorAll(`[id^='sub-${index}-']`);
                
                // Check if any sub-row is visible to determine toggle action
                const isAnyVisible = Array.from(subs).some(sub => sub.style.display === "table-row");

                subs.forEach(function(sub) {
                    if (isAnyVisible) {
                        sub.style.display = "none";
                        mainRow.textContent = "▶";
                    } else {
                        sub.style.display = "table-row";
                        mainRow.textContent = "▼";
                    }
                });
            });
        });
    }

    // Initialize with 'openmain' prefix
    toggleSubRows('openmain');
});
function updateStatus(selectEl) {
    const newStatus = selectEl.value;
    const taskId = selectEl.getAttribute("data-id");

    // 👇 Lấy option đang được chọn
    const selectedOption = selectEl.options[selectEl.selectedIndex];

    // 👇 Lấy màu từ option
    const bgColor = selectedOption.style.backgroundColor;
    const textColor = selectedOption.style.color;
    const borderColor = selectedOption.style.borderColor;

    // 👇 Gán lại style cho <select>
    selectEl.style.backgroundColor = bgColor;
    selectEl.style.color = textColor;
    selectEl.style.border = `1px solid ${borderColor}`;

    // 👇 Gửi AJAX như trước
    fetch("/update-status", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ id: taskId, status: newStatus })
    })
    .then(res => res.json())
    .then(data => {
        console.log("✅ Cập nhật thành công:", data.message);
    })
    .catch(err => {
        console.error("❌ Lỗi khi cập nhật:", err);
    });
}

function reloadPage() {
  location.reload();
}
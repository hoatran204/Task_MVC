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
function showInsertForm(object) {
    const form = document.querySelector(object);
    form.style.display = "block"; 
}
function hiddenInsertForm(object) {
    const form = document.querySelector(object);
    form.style.display = "none"; 
}
function ShowAndHide(selector) {
    const element = document.querySelector(selector);
    const isHidden = window.getComputedStyle(element).display === "none";

    if (isHidden) {
        element.style.display = "block";

        // Thêm trình nghe sự kiện click ra ngoài
        setTimeout(() => {
            function handleClickOutside(e) {
                if (!element.contains(e.target)) {
                    element.style.display = "none";
                    document.removeEventListener("click", handleClickOutside);
                }
            }
            document.addEventListener("click", handleClickOutside);
        }, 0);

    } else {
        element.style.display = "none";
    }
}
function changeAssignment(selectElement) {
    const value = selectElement.value;
    if (value) {
        // Gắn giá trị vào URL dạng ?assignment=value
        window.location.href = `${value}`;
    }
}
function toggleContent(checkbox) {
    const id = checkbox.id.replace(/^id-maintab-/, 'maintab-'); 
    const content = document.getElementById(id);
    if (!content) return;

    if (checkbox.checked) {
        content.classList.remove("hidden");
    } else {
        content.classList.add("hidden");
    }
}
function toggleColumn(index, isVisible) {
  const table = document.getElementById("myTable");

  // Lặp qua tất cả các dòng (tr) trong bảng
  for (const row of table.rows) {
    if (row.cells.length > index) {
      row.cells[index].style.display = isVisible ? "" : "none";
    }
  }
}


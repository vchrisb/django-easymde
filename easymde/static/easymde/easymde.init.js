document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".easymde-box").forEach((elem) => {
    try {
      let options = JSON.parse(elem.getAttribute("data-easymde-options"));
      options["element"] = elem;
      if (!elem.EasyMDE) {
        elem.EasyMDE = new EasyMDE(options);
      }
    } catch (error) {
      console.error("Invalid JSON in data-easymde-options:", error);
    }
  });
});

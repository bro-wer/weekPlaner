function renderCurrentDate() {
  renderCalendar("CURRENT_DATE");
}

function generatePrevMonth() {
  console.log("generatePrevMonth");
  renderCalendar("PREV_MONTH");
}

function generateNextMonth() {
  console.log("generateNextMonth");
  renderCalendar("NEXT_MONTH");
}

function renderCalendar(targetDate) {
    $.ajax({
        url : "renderCalendar/", // the endpoint
        type : "GET", // http method
        data : {
          targetDate : targetDate,
          currentlySetYear : obtainCurrentlySetYear(),
          currentlySetMonth : obtainCurrentlySetMonth()
         }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            document.getElementById("calendarBox").innerHTML = json;
            document.getElementById("messageBox").innerHTML = "";

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
        document.getElementById("messageBox").innerHTML = "<div class=\"alert alert-danger\" role=\"alert\">Failed to render calendar!</div>";
            // $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                // " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function obtainCurrentlySetMonth() {
  var date = obtainTextByElementId("liMonthYearId");
  return date.replace(/\d+/g, '');
}

function obtainCurrentlySetYear() {
  var date = obtainTextByElementId("liMonthYearId");
  return date.replace(/[a-z, A-Z]/g, '');
}


function obtainTextByElementId(elemId) {
  try {
    var html = document.getElementById(elemId).innerHTML;
    var pureText = html.replace(/<[^>]*>/g, "");
    return pureText;
  } catch (e) {
    return "Undefined";
  }
}

//Checks the Query String for any messages that need to be displayed to the user, and displays them on page load.
function displayMessage()
{
    let queryString = (new URL(document.location)).searchParams;

    if(queryString.has("msg"))
    {
        let msgCode = queryString.get("msg");
        if(msgCode in msgCodes) window.onload = function(){
            alert(msgCodes[msgCode]);
        }
    }
}

//On page load
window.onload = function() 
{
    enableModal();
};

//Enables modal for messages
function enableModal()
{
    // Get the modal
    var modal = document.getElementById("msgModal");
    var modalContent = document.getElementById("modalContent");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    //If there are messages, open modal.
    if(modalContent.childNodes.length > 3)
    {
        modal.style.display = "block";
    }
}

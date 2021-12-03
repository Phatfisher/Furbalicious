//On page load
window.onload = function() 
{
    enableModal();
};

//Enables modal for messages
function enableModal()
{
    // Get the modal
    var modal = document.getElementById("myModal");
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
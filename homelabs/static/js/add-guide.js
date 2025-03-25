$(document).ready(function(){

    // Remove the validation error message if there is content 
    $("#form-title").on("blur", function(event) {
        if($(this).val() !== ""){
            $(this).css("border", "");
            var errorSpan = $("#title-section").find('span.error');
            
            if (errorSpan.length > 0) {
                errorSpan.remove(); 
            }
        }

    });

    // Remove the validation error message if select a non default category
    $("#categories").on("change", function() {
        var selectedCategory = $(this).val();  // Get the selected option value
        if($("#categories").val() !== "default"){
            $(this).css("border", "");
            var errorSpan = $("#category-select").find('span.error');
            
            if (errorSpan.length > 0) {
                errorSpan.remove(); 
            }
        }
    });

    // Add and removing prereqs 
    $("#add-prereq-btn").on("click", function(event){
        $("#prerequisites-list").append('<li><textarea placeholder="Enter prerequisite details"></textarea><button class="remove-prereq">✖</button></li>');
    });
    $("#prerequisites-list").on("click", "li button.remove-prereq", function(event) {
        $(this).closest('li').remove();
    });

    // Removes the validation error message if there is content
    $("#prerequisites-list").on("blur", "li textarea", function(event) {
        if($(this).val() !== ""){
            $(this).css("border", "");
            var errorSpan = $(this).closest('li').find('span.error');
            
            if (errorSpan.length > 0) {
                errorSpan.remove();  // Remove the span.error if it exists
            }
        }

    });

    // Add and removing steps 
    $("#add-step-btn").on("click", function(event){
        $("#steps-list").append('<li><textarea placeholder="Enter step details"></textarea><button class="remove-step">✖</button><button class="add-picture">Add Picture?</button><input type="file" class="step-image""></li>');
        var errorSpan = $("#steps-section").find('span.error');
        
        if (errorSpan.length > 0) {
            errorSpan.remove();  // Remove the span.error if it exists
        }
    });

    $("#steps-list").on("click", "li button.remove-step", function(event) {
        $(this).closest('li').remove();
    });

    // Removes the validation error message if there is content
    $("#steps-list").on("blur", "li textarea", function(event) {
        if($(this).val() !== ""){
            $(this).css("border", "");
            var errorSpan = $(this).closest('li').find('span.error');
            
            if (errorSpan.length > 0) {
                errorSpan.remove();  
            }
        }

    });
    
    // Submit the form
    $("#submit-btn").on("click", function(event){
        event.preventDefault();
        validateForm();   
        // Make call to backend
    });
    
    // Add error messages and highlight red if there is missing/invalid content
    function validateForm(){
        var success = true;
        clearErrors();

        if($("#form-title").val() === ""){
            $("#form-title").after('<span class="error"> Please Enter Guide Title.</span>');
            $("#form-title").css("border", "2px solid red");
            success = false;
        } 

        if($("#categories").val() === "default"){
            $("#categories").after('<span class="error"> Please Enter Guide Category.</span>');
            $("#categories").css("border", "2px solid red");
            success = false;
        }

        $("#prerequisites-list li").each(function(_, element) {
            var textarea = $(element).find("textarea");
            if(textarea.val() === ""){
                textarea.after('<span class="error"> Missing Details.</span>');
                textarea.css("border", "2px solid red");
                success = false;
            }
        });

        if ($("#steps-list li").length > 0) {
            $("#steps-list li").each(function(_, element) {
                var textarea = $(element).find("textarea");
                if(textarea.val() === ""){
                    textarea.after('<span class="error"> Missing Details.</span>');
                    textarea.css("border", "2px solid red");
                    success = false;
                }
            });
        } else {
            $("#steps-list").after('<span class="error"> A Guide Needs At Least One Step.</span>');
            success = false;
        }

        return success;
    }  

    function clearErrors(){
        $(".error").hide();
        $("#form-title").css("border", "");
        $("#categories").css("border", "");
        $("#prerequisites-list textarea").css("border", "");
        $("#steps-list textarea").css("border", "");
    }
    
});
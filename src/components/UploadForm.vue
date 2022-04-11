<template>
    <form id="uploadForm" @submit.prevent="uploadPhoto" enctype="multipart/form-data" method="post">
        <input type="file" name="" id="">
        <textarea name="" id="" cols="30" rows="10"></textarea>
        <input @click="uploadPhoto" type="submit" class="btn btn-primary" value="Submit"/>
    </form>

    
</template>

<script>
    export default {

        data() {
            return {
            };
        },
        uploadPhoto() {
            let uploadForm = document.getElementById('uploadForm');
            console.log(uploadForm)
            let form_data = new FormData(uploadForm);
            console.log(form_data)
            
            fetch("/api/upload", {
            method: 'POST',
            body: form_data,
            headers: {'X-CSRFToken': this.csrf_token}
            })
            .then(function (response) {
            return response.json();
            })
            .then(function (data) {
            // display a success message
            console.log(data);
            })
            .catch(function (error) {
            console.log(error);
            });
        },
 
    }
</script>

<style>
</style>
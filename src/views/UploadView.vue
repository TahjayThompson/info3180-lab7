<template>
    <div class="container">
      <div class="text-center">
        <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
        <h1>Upload</h1>
        <UploadForm/>
      </div>
    </div>
</template>
<script>
import UploadForm from "../components/UploadForm.vue";
export default {
    data() {
        return {};
    },
    components: { UploadForm }
}
</script>



<style>
/* Add any component specific styles here */
</style>
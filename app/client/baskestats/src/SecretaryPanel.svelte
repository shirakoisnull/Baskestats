<script>
  import { onMount } from "svelte";

  let isAuthenticated = false;

  onMount(() => {
    const token = localStorage.getItem("jwtToken");
    if (token) {
      isAuthenticated = true;
    } else {
      // Redirect to login if token is not present
      window.location.href = "/login"; // Redirect to your login route
    }
  });
  // This could contain the content for the authenticated page
</script>

{#if isAuthenticated}
  <!-- Your authenticated page content -->
  <h1>Welcome! You are authenticated.</h1>
{:else}
  <!-- Redirecting to login, no content to display here -->
{/if}
<!-- Your content for the authenticated page goes here -->

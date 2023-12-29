<script>
  import { onMount } from 'svelte';
  export let storedUsername; // Receive the username as a prop

  let isAuthenticated = false;

  onMount(() => {
    const token = localStorage.getItem('jwtToken');
    if (token) {
      isAuthenticated = true;
    } else {
      // Redirect to login if token is not present
      window.location.href = '/login'; // Redirect to your login route
    }
  });
</script>

{#if isAuthenticated}
  <h1>Welcome, {storedUsername}!</h1>
  <!-- Your authenticated page content -->
{:else}
  <!-- Redirecting to login, no content to display here -->
{/if}


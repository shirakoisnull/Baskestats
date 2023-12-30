<script>
  import { onMount } from "svelte";
  let usr = localStorage.getItem('username');
  // export let url = "";
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

</script>

{#if isAuthenticated}
  <h1>Welcome, {usr}!</h1>
  
<div class="card">
  <button on:click={console.log("Clicked")}>Team Management</button>
  <button on:click={console.log("Clicked")}>Player Management</button>
  <button on:click={console.log("Clicked")}>Championship Management</button>
</div>
{:else}
  <!-- Redirecting to login, no content to display here -->
{/if}

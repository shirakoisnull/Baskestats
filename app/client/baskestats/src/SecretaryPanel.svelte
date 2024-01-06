<script>
  import { Link } from "svelte-routing";
  import { navigate } from "svelte-routing";
  import { onMount } from "svelte";
  let usr = localStorage.getItem("username");
  // export let url = "";
  let isAuthenticated = false;

  onMount(() => {
    const token = localStorage.getItem("jwtToken");
    if (token) {
      isAuthenticated = true;
    } else {
      // Redirect to login if token is not present
      window.location.href = "/"; // Redirect to your login route
    }
  });
  
  function logout() {
    localStorage.removeItem("jwtToken");
    localStorage.removeItem("username");
    navigate("/");
  }
</script>

{#if isAuthenticated}
  <h1>Welcome, {usr}!</h1>
  <button>
    <Link to="/teams" class="button-link">Team Management</Link>
  </button>
  <button>
    <Link to="/players" class="button-link">Player Management</Link>
  </button>
  <button>
    <Link to="/champ" class="button-link">Champ Management</Link>
  </button>
{/if}

<button class="back-button" on:click={() => navigate("/")}>Home</button>
<button class="logout-button" on:click={() => logout()}>Logout</button>

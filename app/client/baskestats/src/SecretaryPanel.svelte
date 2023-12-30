<script>
  // import { Router, Link, Route } from "svelte-routing";
  // import TeamManagement from "./routes/TeamManagement.svelte";
  // import PlayerManagement from "./routes/PlayerManagement.svelte";
  // import ChampManagement from "./routes/ChampManagement.svelte";
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

  // function goToTeamManagement() {
  //   navigate("./routes/TeamManagement.svelte"); // Redirect to team management route
  // }

  // function goToPlayerManagement() {
  //   navigate("/player-management"); // Redirect to player management route
  // }

  // function goToChampionshipManagement() {
  //   navigate("/championship-management"); // Redirect to championship management route
  // }

</script>


{#if isAuthenticated}
  <h1>Welcome, {usr}!</h1>
  <!-- Your authenticated page content -->
  <!-- <Router {url}>
    <nav>
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
      <Link to="/blog">Blog</Link>
    </nav>
    <div>
      <Route path="/blog" component={Blog} />
      <Route path="/about" component={About} />
      <Route path="/"><Home /></Route>
    </div>
  </Router> -->
<!-- <div class="card">
  <button on:click={goToTeamManagement}>Team Management</button>
  <button on:click={goToPlayerManagement}>Player Management</button>
  <button on:click={goToChampionshipManagement}>Championship Management</button>
</div> -->
{:else}
  <!-- Redirecting to login, no content to display here -->
{/if}

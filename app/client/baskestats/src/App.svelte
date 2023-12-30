<script>
  import Login from "./Login.svelte";
  import { Router, Link,Route } from "svelte-routing";
  import TeamManagement from "./routes/TeamManagement.svelte";
  import PlayerManagement from "./routes/PlayerManagement.svelte";
  import ChampManagement from "./routes/ChampManagement.svelte";
  import SecretaryPanel from "./SecretaryPanel.svelte";
</script>
<!-- <Router>
  <Route path="/team-management" component={TeamManagement} />
  <Route path="/player-management" component={PlayerManagement} />
  <Route path="/championship-management" component={ChampManagement} />
</Router> -->
<SecretaryPanel />
<h1>Baskestats</h1>
<!-- TODO: Replace with BaskeStats Logo/Splash -->

<!-- <TeamManagement /> -->
<main>
  <div class="card">
  <Login />
  </div>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
    will-change: filter;
    transition: filter 300ms;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
  /* .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  } */

  h1:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
</style>

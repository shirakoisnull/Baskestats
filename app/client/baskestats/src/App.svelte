<script>
  import { Router, Route, Link } from 'svelte-routing';
  import Login from './Login.svelte';
  import SecretaryPanel from './SecretaryPanel.svelte';
  import TeamManagement from './routes/TeamManagement.svelte';
  import PlayerManagement from './routes/PlayerManagement.svelte';
  import ChampManagement from './routes/ChampManagement.svelte';
</script>

<Router>
  <Route path="/">
    <!-- Your main page content -->
    <h1>Welcome to BaskeStats</h1>
    <button>
      <Link to="/login" class="button-link">Login</Link>
    </button>
    
  </Route>
  <Route path="/login" component={Login} />
  <Route path="/secretary" component={SecretaryPanel} />
  <Route path="/teams" component={TeamManagement} />
  <Route path="/players" component={PlayerManagement} />
  <Route path="/champ" component={ChampManagement} />
</Router>



<!-- <SecretaryPanel />
<h1>Baskestats</h1>
<!-- TODO: Replace with BaskeStats Logo/Splash -->

<!-- <TeamManagement /> -->
<!-- <main>
  <div class="card">
  <Login />
  </div>
</main>  -->

<style>
 /*  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  } */

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
    will-change: filter;
    transition: filter 300ms;
  }

  /* @media (min-width: 640px) {
    main {
      max-width: none;
    }
  } */
  /* .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  } */

  h1:hover {
    filter: drop-shadow(0 0 2em #ff4000cf);
  }
</style>

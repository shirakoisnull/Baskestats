<script>
  import { Router, Route, Link } from 'svelte-routing';
  import BottomNavigation from './BottomNavigation.svelte'; 
  import Login from './Login.svelte';
  import SecretaryPanel from './SecretaryPanel.svelte';
  import TeamManagement from './routes/TeamManagement.svelte';
  import PlayerManagement from './routes/PlayerManagement.svelte';
  import ChampManagement from './routes/ChampManagement.svelte';
  import TeamCreate from './routes/TeamCreate.svelte';
  import TeamUpdate from './routes/TeamUpdate.svelte';
  import PlayerCreate from './routes/PlayerCreate.svelte';
  import PlayerUpdate from './routes/PlayerUpdate.svelte';
  import ChampCreate from './routes/ChampCreate.svelte';
  import ChampUpdate from './routes/ChampUpdate.svelte';
  import DrawChamp from './routes/DrawChamp.svelte';
  import Test from './routes/Test.svelte';
  import Teams from './userviews/Teams.svelte';
  import Players from './userviews/Players.svelte';
  import Championships from './userviews/Championships.svelte';
</script>

<main>
<Router>
  <Route path="/">
    <!-- Your main page content -->

    <h1 class="title">Welcome to BaskeStats</h1>
<BottomNavigation />

    <button>
      <Link to="/uteams" class="button-link">Teams</Link>
    </button>
    <button>
      <Link to="/uplayers" class="button-link">Players</Link>
    </button>
    <button>
      <Link to="/uchamps" class="button-link">Championships</Link>
    </button>
    <button>
      <Link to="/login" class="button-link">Login</Link>
    </button>
    
  </Route>
  <Route path="/login" component={Login} />
  <Route path="/secretary" component={SecretaryPanel} />
  <Route path="/teams" component={TeamManagement} />
  <Route path="/players" component={PlayerManagement} />
  <Route path="/champ" component={ChampManagement} />
  <Route path="/teamcreate" component={TeamCreate} />
  <Route path="/teamupdate" component={TeamUpdate} />
  <Route path="/newplayer" component={PlayerCreate} />
  <Route path="/editplayer" component={PlayerUpdate} />
  <Route path="/newchamp" component={ChampCreate} />
  <Route path="/editchamp" component={ChampUpdate} />
  <Route path="/draw" component={DrawChamp} />
  <Route path="/test" component={Test} />
  <Route path="/uteams" component={Teams} />
  <Route path="/uplayers" component={Players} />
  <Route path="/uchamps" component={Championships} />
</Router>
</main>
<!-- TODO: Replace with BaskeStats Logo/Splash -->
<!-- <main>
  <div class="card">
  <Login />
  </div>
</main>  -->

<style>
    main {
    text-align: center;
    padding: 1em;
    /* max-width: 240px; */
    margin: 0 auto;
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

  
</style>

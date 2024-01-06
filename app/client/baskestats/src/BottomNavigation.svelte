<script>
  import { navigate } from "svelte-routing";
</script>

<nav class="bottom-nav">
  <button on:click={() => navigate("/")} class="nav-button">Home</button>
  <button on:click={() => navigate("/uteams")} class="nav-button">Teams</button>
  <button on:click={() => navigate("/uplayers")} class="nav-button">Players</button>
  <button on:click={() => navigate("/uchamps")} class="nav-button">Championships</button>
</nav>

<style>
  /* Style the navigation bar */
  .bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-around;
    background-color: #ff3e00;
    padding: 10px 0;
  }

  /* Style the buttons */
  .nav-button {
    color: white;
    padding: 8px 16px;
    border:none;
    border-radius: 10px;
    transition: background-color 0.3s ease-in-out;
    cursor: pointer;
    background-color: transparent;
    outline: none;
  }

  /* Hover effect */
  .nav-button:hover {
    background-color: #242424;
  }
</style>
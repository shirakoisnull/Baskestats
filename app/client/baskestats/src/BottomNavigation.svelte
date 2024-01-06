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
    /* border: 5px solid #242424; */
    padding: 10px 0;
  }

  /* Style the buttons */
 /* Style the buttons */
  .nav-button {
    color: white;
    padding: 12px 24px;
    border: none;
    border-radius: 30px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
    background-color: transparent;
    outline: none;
    font-size: 16px;
  }

  /* Hover effect */
  .nav-button:hover {
    background-color: #242424;
    transform: scale(1.05);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  }
</style>
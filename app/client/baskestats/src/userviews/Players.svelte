<script>
  import { fetchPlayers, viewPlayer } from "../api.js";
  import { onMount } from "svelte";
  import BottomNavigation from "../BottomNavigation.svelte";
  import PlayerModal from "../modals/PlayerModal.svelte";
  let players = [];
  let playerInfo = [];
  let showModal = false;
  let searchQuery = "";

  onMount(async () => {
    players = await fetchPlayers();
  });

  async function handleView(pId) {
    playerInfo = await viewPlayer(pId);
    showModal = true;
  }


  $: visiblePlayers= searchQuery
    ? players.filter((player) => {
        return player[2].toLowerCase().includes(searchQuery.toLowerCase());
      })
    : players;

</script>

{#if showModal}
  <PlayerModal
    {showModal}
    results={playerInfo}
    closeModal={() => (showModal = false)}
  />
{/if}

<BottomNavigation />

<div class="box">
  <input
    class="search-box"
    type="text"
    bind:value={searchQuery}
    placeholder="Search player..."
  />
</div>

<table>
  <thead>
    <tr>
      <!-- NA EXEI ICON ME FATSOULA OR SOMETHING -->
      <th>Name</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {#each visiblePlayers as player}
      <tr>
        <td>{player[2]}</td>
        <td>
          <button on:click={() => handleView(player[0])}>Info</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>

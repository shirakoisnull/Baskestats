<script>
  import { fetchChampionships, fetchMatches } from "../api.js";
  import { onMount } from "svelte";
  import BottomNavigation from "../BottomNavigation.svelte";
  import ChampModal from "../modals/ChampModal.svelte";

  let championships = [];
  let matchInfo = [];
  let showModal = false;
  let searchQuery = "";

  onMount(async () => {championships = await fetchChampionships();});

  async function handleView(cId) {
    matchInfo = await fetchMatches(cId);
    showModal = true;
  }

  $: visibleChamps = searchQuery
    ? championships.filter((champ) => {
        return String(champ[1]).toLowerCase().includes(searchQuery.toLowerCase());
      })
    : championships;

  console.log(championships);
</script>

{#if showModal}
  <ChampModal
    {showModal}
    results={matchInfo}
    closeModal={() => (showModal = false)}
  />
{/if}

<BottomNavigation />

<div class="box">
  <input
    class="search-box"
    type="text"
    bind:value={searchQuery}
    placeholder="Search year..."
  />
</div>
<div class="table-container">
<table>
  <thead>
    <tr>
        <!-- NA EXEI ICON ME FATSOULA OR SOMETHING -->
      <th>Year</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {#each visibleChamps as champ}
      <tr>
        <td>{champ[1]}</td>
        <td>
          <button on:click={() => handleView(champ[0])}>Info</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>
</div>
<script>
  import { fetchChampionships, fetchMatches } from "../api.js";
  import { onMount } from "svelte";
  import BottomNavigation from "../BottomNavigation.svelte";
  import MatchModal from "../modals/MatchModal.svelte";
  let championships = [];
  let matchInfo = [];
  let showModal = false;

  onMount(async () => {championships = await fetchChampionships();});

  async function handleView(cId) {
    matchInfo = await fetchMatches(cId);
    showModal = true;
  }

</script>

{#if showModal}
  <MatchModal
    {showModal}
    results={matchInfo}
    closeModal={() => (showModal = false)}
  />
{/if}

<BottomNavigation />
<table>
  <thead>
    <tr>
        <!-- NA EXEI ICON ME FATSOULA OR SOMETHING -->
      <th>Year</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {#each championships as champ}
      <tr>
        <td>{champ[1]}</td>
        <td>
          <button on:click={() => handleView(champ[0])}>Info</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>

<script>
  import { fetchChampionships } from "../api.js";
  import { onMount } from "svelte";

  let championships = [];

  onMount(async () => {championships = await fetchChampionships();});

    function handleView(champ){

    }

</script>

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
            <button>Info</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>

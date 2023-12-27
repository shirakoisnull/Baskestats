<script>
  let username = '';
  let password = '';

  function handleSubmit() {
    // Handle form submission (validate, authenticate, etc.)
    console.log('Username:', username);
    console.log('Password:', password);
    // Implement your logic to authenticate here
  }
</script>

<form on:submit|preventDefault={handleSubmit}>
  <label>
    Username:
    <input type="text" bind:value={username} />
  </label>
  <label>
    Password:
    <input type="password" bind:value={password} />
  </label>
  <button type="submit">Login</button>
</form>
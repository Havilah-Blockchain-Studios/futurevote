# Future Vote Smart Contract Documentation

## Functions

### DID Contract

#### Constructor

```solidity
constructor() ERC721("FUTUREVOTEDID", "FVD")
```

Initializes the ERC721 token with the name "FUTUREVOTEDID" and the symbol "FVD".

#### mint

```solidity
function mint(string memory _tokenURI, address minter) public onlyOwner returns (uint256)
```

Mints a new token with the specified token URI and assigns it to the minter.

**Parameters:**

- `_tokenURI` (`string`): The URI for the token metadata.
- `minter` (`address`): The address of the account minting the token.

**Returns:**

- (`uint256`): The ID of the newly created token.

### FutureVote Contract

#### registerVoter

```solidity
function registerVoter(string memory voterUri) external returns (bool)
```

Registers a new voter by minting a new DID for the voter.

**Parameters:**

- `voterUri` (`string`): The URI for the voter's DID.

**Returns:**

- (`bool`): Returns `true` if the voter is successfully registered.

#### startElection

```solidity
function startElection(string memory name) external returns (uint256)
```

Starts a new voting session.

**Parameters:**

- `name` (`string`): The name of the election.

**Returns:**

- (`uint256`): The ID of the newly created election.

#### registerCandidate

```solidity
function registerCandidate(address candidate, uint256 electionId) external onlyRegisteredCandidate(candidate) onlyAdmin(electionId) returns (bool)
```

Registers a new candidate for an election.

**Parameters:**

- `candidate` (`address`): The address of the candidate to be registered.
- `electionId` (`uint256`): The ID of the election.

**Returns:**

- (`bool`): Returns `true` if the candidate is successfully registered.

#### vote

```solidity
function vote(address candidate, uint256 electionId) external onlyRegisteredCandidate(candidate) returns (bool)
```

Allows a voter to vote for a candidate in a specified election.

**Parameters:**

- `candidate` (`address`): The address of the candidate to vote for.
- `electionId` (`uint256`): The ID of the election.

**Returns:**

- (`bool`): Returns `true` if the vote is successfully cast.

#### end

```solidity
function end(uint256 electionId) external onlyAdmin(electionId) returns (bool)
```

Ends an election.

**Parameters:**

- `electionId` (`uint256`): The ID of the election to be ended.

**Returns:**

- (`bool`): Returns `true` if the election is successfully ended.

#### changeElectionAdmin

```solidity
function changeElectionAdmin(uint256 electionId, address admin) external onlyAdmin(electionId) returns (bool)
```

Transfers admin ownership of an election to a new account.

**Parameters:**

- `electionId` (`uint256`): The ID of the election.
- `admin` (`address`): The new admin address.

**Returns:**

- (`bool`): Returns `true` if the admin is successfully changed.

#### electionCandidates

```solidity
function electionCandidates(uint256 electionId) external view returns (address[] memory)
```

Returns the list of candidates for a specified election.

**Parameters:**

- `electionId` (`uint256`): The ID of the election.

**Returns:**

- (`address[]`): An array of addresses representing the candidates.

#### checkCandidateExists

```solidity
function checkCandidateExists(address candidate, uint256 id) public view returns (bool)
```

Checks if a candidate exists in a specified election.

**Parameters:**

- `candidate` (`address`): The address of the candidate.
- `id` (`uint256`): The ID of the election.

**Returns:**

- (`bool`): Returns `true` if the candidate exists, `false` otherwise.

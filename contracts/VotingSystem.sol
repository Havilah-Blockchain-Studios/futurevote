/**
 * @title THE FUTURE VOTE SMART CONTRACT
 * @dev This smart contract manages the voting functionality for the Future Vote system.
 * @author GOODNESS E. (COAT)
 * @notice This contract is owned by Havlilah Blockchain Studios, Inc.
 * @dev Created on 15th of May, 2024.
 */

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

/* IMPORT STATEMENTS */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol"; // Importing ERC721 contract for token functionality
import "@openzeppelin/contracts/access/Ownable.sol"; // Importing Ownable contract for access control
import "@openzeppelin/contracts/utils/Counters.sol"; // Importing Counters library for managing token IDs

/**
 * @title IDENTIFICATION SYSTEM CONTRACT
 * @dev This contract manages the identification system for the Future Vote system.
 */
contract DID is ERC721URIStorage, Ownable {
    /* VARIABLE DECLARATION */
    using Counters for Counters.Counter; // Using Counters library for managing token IDs
    Counters.Counter private tokenIds; // Counter for generating unique token IDs

    /**
     * @dev Constructor function to initialize the ERC721 token with the name and symbol.
     */
    constructor() ERC721("FUTUREVOTEDID", "FVD") {}

    /**
     * @dev Mint function to create a new token with the specified token URI.
     * @param _tokenURI The URI for the token metadata.
     * @param minter The address of the account minting the token.
     * @return The ID of the newly created token.
     */
    function mint(string memory _tokenURI, address minter)
        public
        onlyOwner
        returns (uint256)
    {
        uint256 newDidId = tokenIds.current(); // Get the current token ID
        _mint(minter, newDidId); // Mint a new token with the specified owner and ID
        _setTokenURI(newDidId, _tokenURI); // Set the token URI for the newly minted token
        tokenIds.increment(); // Increment the token ID counter for the next token
        return newDidId; // Return the ID of the newly created token
    }
}

/**
 * @title FUTURE VOTE CONTRACT
 * @dev This contract manages the voting functionality for the Future Vote system.
 */
contract FutureVote is Ownable {
    // Your voting functionality code will go here
}

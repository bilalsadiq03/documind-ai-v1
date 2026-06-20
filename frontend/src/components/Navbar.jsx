function Navbar() {
  return (
    <nav className="border-b bg-black text-white">
      <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">

        <h1 className="text-xl font-bold">
          DocuMind AI
        </h1>

        <button
          className="px-4 py-2 border rounded-lg"
        >
          GitHub
        </button>

      </div>
    </nav>
  );
}

export default Navbar;
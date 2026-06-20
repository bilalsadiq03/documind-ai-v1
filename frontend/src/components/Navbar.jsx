function Navbar() {
  return (
    <nav className="border-b bg-white sticky top-0 z-50">

      <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">

        <h1 className="font-bold text-xl">
          DocuMind AI
        </h1>

        <a
          href="https://github.com"
          target="_blank"
          rel="noreferrer"
          className="text-gray-600 hover:text-black"
        >
          GitHub
        </a>

      </div>

    </nav>
  );
}

export default Navbar;
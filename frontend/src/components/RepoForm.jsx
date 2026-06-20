import { useState } from "react";

function RepoForm({ onGenerate, loading }) {
    const [repoUrl, setRepoUrl] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!repoUrl.trim()) {
            return;
        }

        onGenerate(repoUrl);
    };

    return (
        <div className="max-w-3xl mx-auto">

            <form
                onSubmit={handleSubmit}
                className="flex gap-4"
            >

                <input
                    type="text"
                    placeholder="https://github.com/user/repository"
                    value={repoUrl}
                    onChange={(e) => setRepoUrl(e.target.value)}
                    className="flex-1 border rounded-xl px-5 py-4 outline-none"
                />
                <button
                    disabled={loading}
                    type="submit"
                    className="bg-black text-white px-8 rounded-xl disabled:opacity-50 cursor-pointer"
                >
                    {loading ? "Generating..." : "Generate"}
                </button>

            </form>

        </div>
    );
}

export default RepoForm;
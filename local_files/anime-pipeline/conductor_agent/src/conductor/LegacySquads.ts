/**
 * Legacy Squad Mocks
 * Used when the original Squad/Automation code is not present.
 */

// Types
export interface V3Script {
    title: string;
    scenes: V3Scene[];
    characters: V3Character[];
}
export interface V3Scene {
    number: number;
    visualKeyVisuals?: string;
    visualPrompt?: string;
}
export interface V3Character {
    id: string;
    name: string;
}
export interface StyleGuide {
    mood: string;
}

export class StorySquad {
    constructor(private geminiKey: string, private grokKey?: string) {}
    async developStory(theme: string): Promise<V3Script> {
        console.log('[Mock] StorySquad developing story for theme:', theme);
        return {
            title: `Story about ${theme}`,
            scenes: [],
            characters: []
        };
    }
}

export class ArtSquad {
    constructor(private geminiKey: string) {}
    async establishStyle(script: V3Script): Promise<StyleGuide> {
        console.log('[Mock] ArtSquad establishing style');
        return { mood: 'General' };
    }
    async createBackground(description: string, style: StyleGuide): Promise<string> {
        return `<svg>Background for ${description}</svg>`;
    }
    async createCharacter(char: V3Character, action: string, style: StyleGuide): Promise<string> {
        return `<svg>Character ${char.name}</svg>`;
    }
}

export class SoundSquad {
    async castVoices(characters: V3Character[]): Promise<Map<string, unknown>> {
        return new Map();
    }
    async recordScene(scene: V3Scene, voiceMap: Map<string, unknown>): Promise<string> {
        return 'audio.mp3';
    }
}

export class GrokAgent {
    constructor(private apiKey: string) {}
    async generateContent(prompt: string, systemInstruction?: string): Promise<string> {
        return `[Grok Content for: ${prompt}]`;
    }
}
